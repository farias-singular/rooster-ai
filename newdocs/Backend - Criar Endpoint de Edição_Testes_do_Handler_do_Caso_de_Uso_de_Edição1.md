```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public class UpdateBrandHandlerTest
    {
        private readonly IBrandRepository _brandRepository = Substitute.For<IBrandRepository>();
        private readonly IOrganizationRepository _organizationRepository = Substitute.For<IOrganizationRepository>();
        private readonly ICategoryRepository _categoryRepository = Substitute.For<ICategoryRepository>();
        private readonly IUnitOfWork _unitOfWork = Substitute.For<IUnitOfWork>();
        private readonly IMapper _mapper = Substitute.For<IMapper>();
        private readonly UpdateBrandHandler _handler;

        public UpdateBrandHandlerTest()
        {
            _handler = new UpdateBrandHandler(
                _brandRepository,
                _organizationRepository,
                _categoryRepository,
                _unitOfWork,
                _mapper);
        }

        [Fact]
        public async Task Handle_UpdatesBrand()
        {
            // Arrange
            var command = BrandHelper.RandomUpdateBrandCommand();
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var brand = EntityFaker.RandomBrand(id: command.Id, organization: organization, category: category, name: command.Name, title: command.Title);
            var dto = new UpdateBrandDto(brand.Id, organization, category, brand.Name, brand.Title);

            _brandRepository.GetByIdAsync(command.Id).Returns(brand);
            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns(organization);
            _categoryRepository.GetByIdAsync(command.CategoryId).Returns(category);
            _mapper.Map<UpdateBrandDto>(brand).Returns(dto);

            // Act
            var result = await _handler.Handle(command, CancellationToken.None);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(dto.Id, result.Id);
            Assert.Equal(dto.Organization, result.Organization);
            Assert.Equal(dto.Category, result.Category);
            Assert.Equal(dto.Name, result.Name);
            Assert.Equal(dto.Title, result.Title);
            _brandRepository.Received(1).Update(brand);
            await _unitOfWork.Received(1).CommitAsync(CancellationToken.None);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenBrandNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomUpdateBrandCommand();

            _brandRepository.GetByIdAsync(command.Id).Returns((Brand)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Brand not found", exception.Message);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenOrganizationNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomUpdateBrandCommand();
            var brand = EntityFaker.RandomBrand();

            _brandRepository.GetByIdAsync(command.Id).Returns(brand);
            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns((Organization)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Organization not found", exception.Message);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenCategoryNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomUpdateBrandCommand();
            var brand = EntityFaker.RandomBrand();
            var organization = EntityFaker.RandomOrganization();

            _brandRepository.GetByIdAsync(command.Id).Returns(brand);
            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns(organization);
            _categoryRepository.GetByIdAsync(command.CategoryId).Returns((Category)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Category not found", exception.Message);
        }
    }
}
```
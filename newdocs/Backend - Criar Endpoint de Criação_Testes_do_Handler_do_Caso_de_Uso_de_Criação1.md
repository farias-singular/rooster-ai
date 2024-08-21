```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public class CreateBrandHandlerTest
    {
        private readonly IBrandFactory _brandFactory = Substitute.For<IBrandFactory>();
        private readonly IBrandRepository _brandRepository = Substitute.For<IBrandRepository>();
        private readonly IOrganizationRepository _organizationRepository = Substitute.For<IOrganizationRepository>();
        private readonly ICategoryRepository _categoryRepository = Substitute.For<ICategoryRepository>();
        private readonly IUnitOfWork _unitOfWork = Substitute.For<IUnitOfWork>();
        private readonly IMapper _mapper = Substitute.For<IMapper>();
        private readonly CreateBrandHandler _handler;

        public CreateBrandHandlerTest()
        {
            _handler = new CreateBrandHandler(
                _brandFactory, 
                _brandRepository, 
                _organizationRepository, 
                _categoryRepository, 
                _unitOfWork, 
                _mapper);
        }

        [Fact]
        public async Task Handle_CreatesBrand()
        {
            // Arrange
            var command = BrandHelper.RandomCreateBrandCommand();
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var brand = EntityFaker.RandomBrand(id: command.Id, organization: organization, category: category, name: command.Name, title: command.Title);
            var dto = new CreateBrandDto(brand.Id, organization, category, brand.Name, brand.Title);

            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns(organization);
            _categoryRepository.GetByIdAsync(command.CategoryId).Returns(category);
            _brandFactory.Create(command.Id, organization, category, command.Name, command.Title).Returns(brand);
            _mapper.Map<CreateBrandDto>(brand).Returns(dto);

            // Act
            var result = await _handler.Handle(command, CancellationToken.None);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(dto.Id, result.Id);
            Assert.Equal(dto.Organization, result.Organization);
            Assert.Equal(dto.Category, result.Category);
            Assert.Equal(dto.Name, result.Name);
            Assert.Equal(dto.Title, result.Title);
            await _brandRepository.Received(1).CreateAsync(brand);
            await _unitOfWork.Received(1).CommitAsync(CancellationToken.None);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenOrganizationNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomCreateBrandCommand();

            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns((Organization)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Organization not found", exception.Message);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenCategoryNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomCreateBrandCommand();
            var organization = EntityFaker.RandomOrganization();

            _organizationRepository.GetByIdAsync(command.OrganizationId).Returns(organization);
            _categoryRepository.GetByIdAsync(command.CategoryId).Returns((Category)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Category not found", exception.Message);
        }
    }
}
```
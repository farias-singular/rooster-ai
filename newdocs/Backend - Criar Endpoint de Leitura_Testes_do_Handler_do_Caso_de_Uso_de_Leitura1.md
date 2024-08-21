```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public class GetBrandByIdHandlerTest
    {
        private readonly IBrandRepository _brandRepository = Substitute.For<IBrandRepository>();
        private readonly IMapper _mapper = Substitute.For<IMapper>();
        private readonly GetBrandByIdHandler _handler;

        public GetBrandByIdHandlerTest()
        {
            _handler = new GetBrandByIdHandler(_brandRepository, _mapper);
        }

        [Fact]
        public async Task Handle_ReturnsBrand()
        {
            // Arrange
            var query = BrandHelper.RandomGetBrandByIdQuery();
            var brand = EntityFaker.RandomBrand(id: query.Id);
            var dto = new GetBrandByIdDto(brand.Id, brand.Organization, brand.Category, brand.Name, brand.Title);

            _brandRepository.GetByIdAsync(query.Id).Returns(brand);
            _mapper.Map<GetBrandByIdDto>(brand).Returns(dto);

            // Act
            var result = await _handler.Handle(query, CancellationToken.None);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(dto.Id, result.Id);
            Assert.Equal(dto.Organization, result.Organization);
            Assert.Equal(dto.Category, result.Category);
            Assert.Equal(dto.Name, result.Name);
            Assert.Equal(dto.Title, result.Title);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenBrandNotFound()
        {
            // Arrange
            var query = BrandHelper.RandomGetBrandByIdQuery();

            _brandRepository.GetByIdAsync(query.Id).Returns((Brand)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(query, CancellationToken.None));
            Assert.Equal("Brand not found", exception.Message);
        }
    }
}
```